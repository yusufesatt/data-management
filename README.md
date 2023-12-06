# Data Management Tools 

<p><b>This repository contains various tools for data management and organization.</b></p>

<p><b>It includes tools that facilitate various tasks such as performing operations on data sets, cleaning empty data, calculating class counts, etc.</b></p>

- [Empty Data Remover](#empty-data-remover)

## Tools 

<h3 id="empty-data-remover">Empty Data Remover</h3>

This tool deletes both the image and the label files of the data that have empty label txt's in the dataset.

#### Sample folder schema:
**Warning! :** In the root folder, except for train, test, and valid folders, only txt and yaml files can be found, do not add files with different extensions.

<pre>
├─data
    ├─train
        ├─images
        ├─labels
    ├─test
        ├─images
        ├─labels
    ├─valid
        ├─images
        ├─labels
</pre>


#### Use Case:
##### Note: Currently only works for data in txt format.

```bash
python empty_data_remover.py --input_path path/to/your/root/folder
```

### Contribution
<hr>

#### If you want to contribute to this project, please open a new issue or submit a merge request. Waiting for your contributions 🚀