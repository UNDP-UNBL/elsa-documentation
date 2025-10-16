# R Projects

## Why Use R Projects?
*R* Projects provide a structured way to organize your work in *R*. They help manage 
file paths, working directories, and dependencies, ensuring that code runs consistently. Benefits include:

- **Self-contained workflows**: Keeps all scripts, data, and outputs in one directory.
- **Automatic working directory management**: Avoids the need to use `setwd()`, ensuring 
  that paths remain consistent.
- **Version control integration**: Works seamlessly with Git and GitHub.
- **Easier collaboration**: Facilitates sharing and replicability of projects.

## Setting Up an R Project

#### Creating a New R Project
To create a new R Project in **RStudio**:

1. Open **RStudio**.
2. Go to **File → New Project...**.
3. Choose **New Directory**.
4. Select **Empty Project** (you can also use project templates, but ww will not go into tha there).
5. Choose a directory name and location.
6. Click **Create Project**.

RStudio will now open the new project with a `*.Rproj` file, managing paths automatically.

#### Using an Existing Directory as an R Project
To convert an existing directory into an R Project:

1. Open **RStudio**.
2. Go to **File → New Project...**.
3. Choose **Existing Directory**.
4. Browse to the directory and click **Create Project**.

RStudio will create a `*.Rproj` file inside the folder, enabling project-based workflows.

Now, whenever you open the `*.Rproj` file, RStudio will set the working directory correctly.

