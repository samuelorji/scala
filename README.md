# Scala Zone Content
This repository contains content of ScalaZONE website. It stores both lessons text and overall courses structure. Everyone is welcome to make PRs with suggestions [TODO contributing.md]

## Deployment triggers
 - Every commit to `develop` brach updates the content on development environment.
 - Every commit to `stage` brach updates the content on staging environment.
 - Every commit to `master` brach updates the content on production environment.
Only production environment is accessible to the public. [TODO: add access for other people?]

## Structure overview

### Courses

Courses are the top-level entity in the ScalaZONE material structure. Their structure is stored in the [courses](/courses) directory. [courses/index.json](/courses/index.json) files stores a list with all availalble courses. For each course there is a directory named after the course id that contains the course structure. Basic course data is stored in the index.json file in this directory. This json has following fields:
| Field name | Type            | Description                                                                                   |
|------------|-----------------|-----------------------------------------------------------------------------------------------|
| `name`     | String          | Name of the course that is visible on the website.                                            |
| `levels`   | List of strings | List of strings - Available levels of the course. Levels are described in the next paragraph. |
| `image`    | String          | Path of the image of the course, it has to refer to an image inside this repository.          |
| `video`    | String          | Video link that is displayed on the course overview page.                                     |
| `desc`     | String          | Description of the course.                                                                    |
| `scope`    | List of string  | Scope of the course. These are presented in the bullet list on the course overview page.      |

### Course Levels

Course levels are parts of the course that are suited for users with different levels of understanding of the material. There are three levels that are possible to add to a course:
 - Beginner
 - Intermediate
 - Advanced
 To add a level to a course, it must be present in the `levels` field in the course's index.json file. Level can be configured using `<level>.json` file in the course directory, where `<level>` is either `beginner`, `intermediate` or `advanced`. This json has following fields:
| Field name | Type                       | Description                                                 |
|------------|----------------------------|-------------------------------------------------------------|
| `name`     | String                     | Name of the course level that is visible on the level page. |
| `desc`     | String                     | Description of the course level.                            |
| `ranges`   | List of TopicRange objects | Defines lessons and topics that are present in the level.   |
And the `TopicRange` type has the following structure in json:
TODO