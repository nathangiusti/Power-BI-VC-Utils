# Deserialize PBIX Files

GitHub Action for pretty printing Power BI Dataflow JSON and PBIX report JSON. 

Takes in a list of files. 

For all .json (dataflow) files, pretty prints 

For all .pbix report files deserializes and pretty prints report json.
- Folder is created with the name of the PBIX file
- For each section, a file is created in the new folder with the section JSON
- The rest of the report is put in a separate json file with the same name as the folder/pbix

For a file "ExampleReport.pbix" with "Section 1", "Section 2", and "Section 3" will create a folder called "ExampleReport" with 4 files inside:
- ExampleReport.json
- Section_1.json
- Section_2.json
- Section_3.json

Takes as input files, a space delineated list of json and PBIX files to iterate over. 

# Usage

```yaml
name: Reformat Power BI Assets
on: [pull_request]
jobs:
  Reformat-Power-BI-Assets:
    runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v2
      with:
        fetch-depth: 0
    - name: Get changed files
      id: changed-files
      uses: tj-actions/changed-files@v19
      with:
        separator: ","
        quotepath: true
    - name: Power BI VC Utils
      uses: nathangiusti/Power-BI-VC-Utils@v2.5
      with:
        files: ${{ steps.changed-files.outputs.all_modified_files }}
        separator: ","
    - uses: stefanzweifel/git-auto-commit-action@v4
      with:
        commit_message: Reformatted files for VC
```

|               Input               |          type          | required |        default        |                                                                                                                                                          description                                                                                                                                                          |
|:---------------------------------:|:----------------------:|:--------:|:---------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| files | `string` | `true` | | List of files to process. Will only deploy files with .pbix ending. The rest will be ignored. |
| separator | `string` | `false` | `","` | Character which separates file names. |
