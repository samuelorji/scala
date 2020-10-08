# Scala Zone Content
This repository contains content of ScalaZONE website. It stores both lessons text and overall courses structure. Everyone is welcome to make PRs with suggestions [TODO contributing.md]

## Deployment triggers
 - Every commit to `develop` brach updates the content on development environment.
 - Every commit to `stage` brach updates the content on staging environment.
 - Every commit to `master` brach updates the content on production environment.
Only production environment is accessible to the public. [TODO: add access for other people?]

## Structure overview

### Courses

Courses are the top-level entity in the ScalaZONE material structure. Their structure is stored in the [courses](/courses) directory. [courses/index.json](/courses/index.json) files stores a list with all available courses. For each course there is a directory named after the course id that contains the course structure. Basic course data is stored in the index.json file in this directory. `Course` JSON type  structure:

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
 To add a level to a course, it must be present in the `levels` field in the course's index.json file. Level can be configured using `<level>.json` file in the course directory, where `<level>` is either `beginner`, `intermediate` or `advanced`. `Level` JSON structure:

| Field name | Type                       | Description                                                 |
|------------|----------------------------|-------------------------------------------------------------|
| `name`     | String                     | Name of the course level that is visible on the level page. |
| `desc`     | String                     | Description of the course level.                            |
| `ranges`   | List of TopicRange objects | Defines lessons and topics that are present in the level.   |

And the `TopicRange` type has the following structure in json:

| Field name    | Type   | Description                                               |
|---------------|--------|-----------------------------------------------------------|
| `topicId`     | String | Id of the topic                                           |
| `lessonStart` | String | Id of the first lesson of the topic included in the level |
| `lessonEnd`   | String | Id of the last lesson of the topic included in the topic  |

Topic ranges define what topics and lessons are present in a course level. By using this entity we are able to use only part of a topic in a course level. 

### Topics

Topics are ordered collections of lessons. Their index is stored at [topics/index.json] file. Structure of a signle topic is defined in the `index.json` file inside the specific directory named after the topic in the `topics` directory. This `index.json` file has following JSON structure:

| Field name | Type           | Description                                      |
|------------|----------------|--------------------------------------------------|
| `name`     | String         | Name of the topic that is visible on the website |
| `desc`     | String         | Description of the topic                         |
| `lessons`  | List of Lesson | Lessons that this topic consists of              |

`Lesson` JSON type structure:

| Field name      | Type            | Description                                               |
|-----------------|------------------|-----------------------------------------------------------|
| `id`            | String          | Id of the lessons                                         |
| `title`         | String          | Title of the lesson - name that is visible on the website |
| `authorId`      | String          | Id of the lesson's author                                 |
| `duration`      | Int             | Expected duration of lesson completion in minutes         |
| `prerequisites` | List of String  | Ids of lessons that are prerequisites of this lesson         |

### Lessons

Lesson's content files are present in the topics directory, within a directory specific to the lesson's topic. Content file has to be named after the lesson id and have a `.md` file extension. This file defines the text and questions that user sees after entering the lesson page. 
You can use most of the markdown features inside of it, including tables, images and a special syntax for videos.

#### Video syntax
To embed a video inside a lesson you can use the following syntax:

```md
[![alt text](alt image link)](embeddable video link)
```

#### Questions section

The first part of every lesson's markdown file is the lesson's content - the text that is visibile on the lessons page and is meant to explain a concept specific to this lesson. After this first part, it is possible to include questions testing the user's knowledge at the end of the lesson. To do so you have to introduce the questions section separator: `?---?` and write your questions after it. At this moment there are two types of questions - `single answer questions` and `multiple answer questions`. Every question begins with a single-hash markdown header, for example:

```md
# How much is 1+1?
```

It is possible to include code blocks, tables and other markdown elements that are not children of the header element. They have to be present after the header element.

After the question, you have to provide the question's answer choices. You do it using unordered markdown list. It can be either defined using dashes (`-`) or bullets (`*`). However, the character you choose defines the type of the question. Dashes are used for single answer question and bullets for multiple answer questions. To indicate whether the answer is correct you have to use the markdown's checkboxes that come after the list character. Two examples below present this behaviour:

Single answer question:
~~~md
# What is the result of expression below?

```
2+2
```

 - [ ] 3
 - [X] 4
 - [ ] 7
~~~

Multiple answer question:
~~~md
# What is the result of expression below?

```
2+2
```

 * [ ] 3
 * [X] 4
 * [ ] 7
 * [X] Four
~~~

To sum it up, let's look on a sample lesson containing a mock content and two questions:

~~~md
# Addition

To add two numbers ...

# Substraction

...

?---?

# What is the result of `2+2` expression?

 - [ ] 3
 - [X] 4
 - [ ] 7

# What is the result of expression below?

```
2+2
```

 * [ ] 3
 * [X] 4
 * [ ] 7
 * [X] Four

```
~~~

### Authors

Courses' authors are defined in the [authors.json](/authors.json) file. This file contains a list of `Author` objects. The `Author` JSON object has following structure:

| Field name | Type             | Description                                 |
|------------|------------------|---------------------------------------------|
| `id`       | String           | Id of the author                            |
| `name`     | String           | Name that is presented on the website       |
| `order`    | Int              | The order of the author in the authors list |
| `twitter`  | String, Optional | Link to the author's twitter page           |
| `github`   | String, Optional | Link to the author's github page            |
| `desc`     | String           | Description of the author                   |