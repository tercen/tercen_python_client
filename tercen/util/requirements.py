import sys
import subprocess
import csv
import glob
import os


def get_base_prefix_compat():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

if get_base_prefix_compat() == sys.prefix:
    "No virtual environment active."


venvPath = sys.prefix
venvName = str.split(venvPath, '/')[-1]

srcFolder = "/home/thiago/Tercen/repos/tercen_python_client/tercen/"

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

        pkgDict = {'name':pkgName, 'version':pkgParts[1], 'requires':[]}
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
                    "#egg==", modul]))
    else:
        for p in distPkgs:
            if modul == p["name"]:
                addedMods.append(p["name"])
                reqs = p["requires"]
                for r in reqs:
                    if not r in addedMods:
                        addedMods.append(r)
                break

# Turn the modules into a module string
for m in addedMods:
    for p in distPkgs:
        if m == p["name"]:
            print(''.join([p["name"], '==', p["version"] ]))

for r in fullReqs:
    print(r)
            