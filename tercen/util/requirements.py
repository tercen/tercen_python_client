import sys
import subprocess
import csv
import glob
import os
import json


def get_base_prefix_compat():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

if get_base_prefix_compat() == sys.prefix:
    "No virtual environment active."


venvPath = sys.prefix
venvName = str.split(venvPath, '/')[-1]

if len(sys.argv) <= 1:
    raise "Base folder is required to detect requirements"



srcFolder = ''.join([os.path.abspath(sys.argv[1]), '/'])

if not os.path.exists:
    raise "Given source path does not exist"

subprocess.call(["pipreqs", "--force", srcFolder], 
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT)


reqModules = []
with open(srcFolder + 'requirements.txt', newline='') as csvfile:
    reqReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reqReader:
        reqModules.append( str.split(row[0], "==")[0] )


distPkgs = []
eggPkgs = []

venvPythDist = glob.glob(''.join([venvPath, '/lib/python3*']) )[0]
venvPkgs = glob.glob(''.join([venvPythDist, '/site-packages/*']))
venvSrcPkgs = glob.glob(''.join([venvPath, '/src/*']))

vp = venvPkgs[63]

str.split('pexpect\n', '\n')

for vp in venvPkgs:
    if str.endswith(vp, 'dist-info'):
        pkg = str.split(vp, '.dist')[0]
        pkg = str.split(pkg, '/')[-1]
        pkgParts = str.split(pkg, '-')
        
        pkgGit = None
        if os.path.exists( ''.join([vp, '/direct_url.json']) ):
            with open(''.join([vp, '/direct_url.json'])) as f:
                jsonData = json.load(f)
            
            pkgGit = ''.join([ 'git+', jsonData["url"], "@", jsonData["vcs_info"]["requested_revision"]  ])
        
        reqPkgs = []
        with open(''.join([vp, '/METADATA'])) as f:
            lines = f.readlines()

        for l in lines:
               
            if str.startswith(l, 'Requires-Dist'):
                reqPkg = str.split(l, ": ")[1]
                reqPkg = str.split(reqPkg, " ")[0]
                reqPkg = str.split(reqPkg, ";")[0]
                reqPkg = str.split(reqPkg, "\n")[0]
                reqPkg = str.split(reqPkg, ",")[0]
                reqPkg = str.split(reqPkg, "==")[0]
                reqPkg = str.split(reqPkg, ">=")[0]
                reqPkg = str.split(reqPkg, ",=")[0]

                reqPkgs.append(reqPkg)

            if str.startswith(l, 'Name: '):
                
                pkgName = str.split(l, ": ")[1]
                pkgName = str.split(pkgName, "\n")[0]
                version = pkgParts[1]

                if not pkgGit is None:
                    version = pkgGit
                

        pkgDict = {'name':pkgName, 'version':version, 'requires':[]}
        pkgDict["requires"] = reqPkgs
        distPkgs.append(pkgDict)
        
# Packages distributed as source/egg (such as pytson)
for vp_ in venvSrcPkgs:
    vp = glob.glob(''.join([vp_, '/*egg-info']))[0]
    if str.endswith(vp, '.egg-info'):
        
        pkg = str.split(vp, '.egg')[0]
        pkg = str.split(pkg, '/')[-1]
        
        with open(''.join([vp, '/PKG-INFO'])) as f:
            lines = f.readlines()

        for l in lines:
            if str.startswith(l, "Version"):
                version = str.split(l, ": ")[-1]
                version = str.split(version, "\n")[0]

        pkgDict = {'name':pkg, 'version':version}

        for i in range(0, len(reqModules)):
            if reqModules[i] == pkg:
                reqModules[i] = reqModules[i] + '.egg'
        
        eggPkgs.append(pkgDict)
        


fullReqs = []
addedMods = []

for modul in reqModules:

    if str.endswith(modul, '.egg'):
        
        modul = str.split(modul, '.egg')[0]

        modulInfo = subprocess.check_output(['python3', '-m', 'pip', 'show', modul])
        modulInfo = modulInfo.decode("utf-8")
        lines = str.split(modulInfo, '\n')
        for l in lines:
            if str.startswith(l,"Location"):
                loc = str.strip(str.split(l, ':')[-1])
            if str.startswith(l,"Version"):
                version = str.strip(str.split(l, ':')[-1])

        eggInstall = subprocess.check_output([
            'python3', '-m', 'pip', 'freeze', '--path', loc
        ]) 
        eggInstall = eggInstall.decode("utf-8")

        eggInstall = str.split(eggInstall, '@')[0]
        
        for p in eggPkgs:
            if modul == p["name"]:
                fullReqs.append(''.join([eggInstall, "@", p["version"], 
                    "#egg=", modul]))
    else:
        for p in distPkgs:
            if modul == p["name"]:
                addedMods.append(p["name"])
                reqs = p["requires"]
                for r in reqs:
                    if not r in addedMods:
                        addedMods.append(r)
                


# Turn the modules into a module string
# Some are options, so they might no actually be installed
for m in addedMods:
    for p in distPkgs:
        if m == p["name"]:
            if str.startswith(p["version"], 'git+' ):
                print(p["version"])
            else:
                print(''.join([p["name"], '==', p["version"] ]))



for r in fullReqs:
    print(r)
            