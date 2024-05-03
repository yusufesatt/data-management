# Data Management Tools 

<p><b>This repository contains various tools for data management and organization.</b></p>

<p><b>It includes tools that facilitate various tasks such as performing operations on data sets, cleaning empty data, calculating class counts, etc.</b></p>

- [Empty Data Remover](#empty-data-remover)
- [Txt Class Counter](#class-counter)

## Tools 

<h3 id="empty-data-remover">1. Empty Data Remover</h3>

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
<hr>

<h3 id="class-counter">2. Txt Class Counter</h3>


This project calculates how many annotations there are for each class by reading the txt files in the specified folder.

This allows you to understand whether your data is balanced or unbalanced. 

**Note:** This tool only works for data in txt format but will soon support coco format

#### Use Case:

```bash
python txt_class_count.py --input_path path/to/your/dataset/train
```

#### Output:

```bash
Category ID: 1 Number of Annotations: 100
Category ID: 2 Number of Annotations: 200
Category ID: 3 Number of Annotations: 300
Total number of annotations: 600
```

<hr>

## Contributing

If you encounter issues or have suggestions for improvements, please report them on the GitHub repository 🚀.

## License

This project is licensed under the [MIT License](https://github.com/yusufesatt/data-management/?tab=MIT-1-ov-file).
