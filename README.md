# Folder Structure Creator
This tool, built with Python and the Tkinter library, offers a user-friendly interface for generating folder
and file structures based on a provided JSON schema. It's particularly useful for initializing projects, with
a specific focus on Django, but its adaptability allows for use with other projects as well.

## Input Format
To use the Folder Structure Creator, you need to specify the desired folder and file structure in JSON format.
This approach lets you detail the names of folders and files, as well as their hierarchical relationships.

The input schema should follow this example:

```json
{
  "name": "project_name",
  "files": [
    "manage.py"
  ],
  "subdirectories": [
    {
      "name": "project_name",
      "files": [
        "__init__.py",
        "settings.py",
        "urls.py",
        "wsgi.py"
      ],
      "subdirectories": [
        {
          "name": "apps",
          "files": [],
          "subdirectories": [
            {
              "name": "app1",
              "files": [
                "__init__.py",
                "models.py",
                "views.py"
              ],
              "subdirectories": []
            },
            {
              "name": "app2",
              "files": [
                "__init__.py",
                "models.py",
                "views.py"
              ],
              "subdirectories": []
            }
          ]
        },
        {
          "name": "templates",
          "files": [],
          "subdirectories": []
        },
        {
          "name": "static",
          "files": [],
          "subdirectories": [
            {
              "name": "css",
              "files": [],
              "subdirectories": []
            },
            {
              "name": "js",
              "files": [],
              "subdirectories": []
            }
          ]
        }
      ]
    }
  ]
}
```
You can create a sophisticated and intricate structure for your project, paying thorough attention to all
the optimal relationships between different modules. Once it's ready, with just a click, you can have all
these files and folders created.

## Installation
1. Clone the repository:
    
    ```bash
    git clone https://github.com/luxuriant777/Folder-Structure-Generator
    ```

2. Ensure Python is Installed:

    ``` bash
    python --version
    ```
    
    or
    ```bash
    python3 --version
    ```
    
    If Python is installed, the version number will be displayed. If not, you will need to install it.

3. Tkinter comes pre-installed with the standard Python distribution, so you should not need to install 
it manually. If for some reason it is not installed, you can use the following command:

    ```bash
    pip install tk
    ```
    
    or
    
    ```bash
    pip3 install tk
    ```

## Usage
1. Navigate to the cloned repository:

    ```bash
    cd awesome-generator
    ```

2. Run the script using the following command:
    
    ```bash
    python fs-maker.py
    ```
    
    or
    
    ```bash
    python3 fs-maker.py
    ```

3. Once you have defined the desired folder and file structure in JSON format, input it in the corresponding
    form:

    ![Screenshot_1](https://github.com/luxuriant777/awesome-generator/assets/20545475/8180470f-5dc0-4e3d-9e22-65e3a53e3a92)

    The default template may be deleted.

4. Press the button "Create Structure".

5. Select folder where your structure will be generated.

6. That's it! Once you click "Select Folder" the process is finished. Visit your selected folder and enjoy
   the result.

Please ensure that your input is correctly formatted to prevent errors. Improperly formatted JSON may cause
the tool to malfunction or fail. If you're uncertain about the format, consider validating your schema using
the example provided either during script initialization or within this README.md file.

## License
This project is licensed under the terms of the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
This license allows you to use, modify, and distribute the software, provided that any modifications
are also distributed under the same license.

## Contributing
We welcome contributions from the community to help improve this project. Whether you're fixing bugs, adding
new features, or updating documentation, your efforts are greatly appreciated. Please create a `pull` request 
on the `dev` branch or report an issue.

## Disclaimer
While every effort has been made to ensure the accuracy and reliability of this software, it is provided "as is",
without warranty of any kind, expressed or implied. This encompasses any assurances of suitability for a
specific purpose or non-infringement. The authors hold no liability for claims, damages, or any other liabilities
that might arise in connection with the software, its usage, or any related dealings.

End-users bear the sole responsibility of deeming its appropriateness for use and accepting all inherent risks. 
These risks may include, among others, program errors, data loss or damage, equipment failure, or operational 
interruptions.