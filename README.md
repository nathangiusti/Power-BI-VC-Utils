# Power-BI-VC-Utils

NOTE: It is easier to use the following composite action to set up your GitHub/PowerBI integration:
https://github.com/nathangiusti/PBIX-Deserializer

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

Example use:
	
~~~~
name: Reformat Power BI Assets
on: [pull_request]
jobs:
  Reformat-Power-BI-Assets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          ref: ${{ github.head_ref }}
      - id: files
        uses: jitterbit/get-changed-files@v1
      - name: Power BI VC Utils
        uses: nathangiusti/Power-BI-VC-Utils@v1.2
        with:
          files: ${{ steps.files.outputs.all }}
      - uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: Reformatted files for VC
~~~~
