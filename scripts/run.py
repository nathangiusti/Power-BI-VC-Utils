import zipfile
import json
import sys
import os.path

# The characters are illegal in file names and will be replaced with _
ILLEGAL_PATH_CHARACTERS = {'<', '>', ':', '/', '\\', '|', '?', '*', ' ', '(', ')'}

for file in sys.argv:
    # For JSON files, just read and pretty print
    if file.endswith('.json') and os.path.exists(file):
        with open(file, 'r', encoding='utf-8-sig') as f:
            json_str = json.dumps(json.load(f), indent=4)
        with open(file, 'w') as f:
            f.write(json_str)
        print('Pretty Printed {}'.format(file))

    if file.endswith('.pbix') and os.path.exists(file):
        # Get the PBIX file name to use as the directory name
        json_dir_path = file[:-5]

        # Create the directory if it doesn't exist. Remove all existing files from directory if it does
        os.makedirs(json_dir_path, exist_ok=True)
        for f in os.listdir(json_dir_path):
            os.remove(os.path.join(json_dir_path, f))

        # PBIX is just a zip with utf-16-le encoding
        zf = zipfile.ZipFile(file)
        data = json.loads(zf.read('Report/Layout').decode('utf-16-le'))
        data['config'] = json.loads(data['config'])
        if 'filters' in data:
            data['filters'] = json.loads(data['filters'])

        # Remove and process sections separately from the rest of the document
        sections = data.pop('sections')
        for section in sections:
            for visual_container in section['visualContainers']:
                for key in ['config', 'filters', 'query', 'dataTransforms']:
                    if key in visual_container.keys():
                        visual_container[key] = json.loads(visual_container[key])
            section_name = section['displayName'].translate({ord(x): '_' for x in ILLEGAL_PATH_CHARACTERS})
            output_path = json_dir_path + '/' + section_name + '.json'
            with open(output_path, "w") as f:
                json.dump(section, f, indent=4)

        # Dump rest of the PBIX JSON
        file_name = os.path.basename(file)[:-5]
        with open(json_dir_path + '/' + file_name + '.json', "w") as f:
            json.dump(data, f, indent=4)

        print('Pretty Printed {}'.format(file))
