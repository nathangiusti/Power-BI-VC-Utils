import zipfile
import json
import sys
import os.path

for file in sys.argv:
    if file.endswith('.json') and os.path.exists(file):
        with open(file, 'r') as f:
            json_str = json.dumps(json.load(f), indent=4)
        with open(file, 'w') as f:
            f.write(json_str)
        print('Pretty Printed {}'.format(file))
    if file.endswith('.pbix') and os.path.exists(file):
        zf = zipfile.ZipFile(file)
        data = json.loads(zf.read('Report/Layout').decode('utf-16-le'))
        data['config'] = json.loads(data['config'])
        for section in data['sections']:
            for visual_container in section['visualContainers']:
                for key in ['config', 'filters', 'query', 'dataTransforms']:
                    if key in visual_container.keys():
                        visual_container[key] = json.loads(visual_container[key])
        output_path = file[:-5] + '.json'
        with open(output_path, "w") as f:
            json.dump(data, f, indent=4)
        print('Pretty Printed {}'.format(file))
