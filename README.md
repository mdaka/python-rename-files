# Python rename images by width and height
    Select a folder path to rename images depends on width and height

## Example
#### Source folder
![source folder](./imgs/color_wheel_icons_min.png)
#### New Generated folder
![dest folder](./imgs/new_generated_folder_min.png)
#### Copied files with new names
![generated icons](./imgs/new_generated_files_min.png)

## Usage

    [ python script_path prefix_icon_name dest_folder_name src_folder_path ]

    python              => Command to run the script file
    script_path         => Location to the python script, in this package it is called main.py
    prefix_icon_name    => Prefix name for each new generated files of type of image
    dest_folder_name    => New destination folder name where you need the new images to be generated on
    src_folder_path     => The source folder path where are found the original icons 
                           that we need to copy the same file but with a different name
## Script

    python C:\python-rename-files\src\main.py prefix_icon_name new_folder_name src_folder_path

![script output after run](./imgs/script_output_after_run.png)


## Credits

- [Mohammad Daka](https://github.com/mdaka)
- [All Contributors](../../contributors)

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.