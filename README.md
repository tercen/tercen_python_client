
# Python Client

Python 3.9 implementation of the Tercen API and context.







### API Reference

#### Generate depencies

```bash
  python3 -m tercen.util.requirements PATH > requirements.txt
  E.g.: python3 -m tercen.util.requirements ./tercen > requirements.txt
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `PATH` | `string` | **Required**. Module path for which to generate dependencies |

#### Create Tercen Context

```python
  from tercen.client import context as ctx

  tercenCtx = ctx.TercenContext()  # OR
  tercenCtx = ctx.TercenContext(workflowId='WORKFLOW_ID',
                            stepId='STEP_ID')
```

| Parameter | Type     |
| :-------- | :------- |
| `workflowId`      | `string` |
| `stepId`      | `string` | 


#### Save operator results for Development

```python
    df = calc_mean(data)
    df = tercenCtx.add_namespace(df) 
    resDf = tercenCtx.save_dev(df)
```

`tercenContext.save_dev` is functionally identical to `tercenContext.save`,
but it returns the computed table so it can be used in tests.


#### WorkflowBuilder Class

The `WorkflowBuilder` provide functions to easily create workflows and steps programmatically
using the TercenAPI. 


##### _Create Workflow_
```python
    import tercen.util.builder as bld

    wkfBuilder = bld.WorkflowBuilder()
    wkfBuilder.create_workflow( 'PROJECT_NAME', 'WORKFLOW_NAME')
```
If a project matching the name does not exist, one will be created. The same is valid for the workflow.

##### _Add a table step_

```python
    wkfBuilder.add_table_step( DATA )  #OR
    wkfBuilder.add_table_step( DATA_PATH )  
```
Creates a table step with the provided data.

##### _Add a data step_

```python
    wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"}, 
                            columns=[{"name":"Rating.Imaging", "type":"string"}],
                            rows=[{"name":"Rating.Effectiveness", "type":"string"}],
                            labels=[{"name":"Facility.Name", "type":"string"}],
                            colors=[{"name":"Facility.Type", "type":"string"}])
```
Creates a data step with the specified projection and links it to the table step.


## Roadmap

- Save relations and table lists

- Add support for multiple workflow steps in the `WorkflowBuilder`

- Add support for installing and running operators in the `WorkflowBuilder`


### See Also

[teRcenAPI](https://github.com/tercen/teRcenApi)
, [teRcen](https://github.com/tercen/teRcen)
, [teRcenHttp](https://github.com/tercen/teRcenHttp)
, [simple python operator](https://github.com/tercen/simple_python_docker_operator)