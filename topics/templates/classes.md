# Classes

The `object` keyword allows us to create "one-off" instances of objects with state and methods (collectively, we
will call these _members_), but we often need to create multiple instances of similar objects; a _class_ of
objects.

A _class_ allows us to define a body, similar to an object's body with the same members, and to create new
instances of it on demand. Let's convert our `BasicLog` object into a class:

```scala
class BasicLog():
  val writer: FileWriter = FileWriter("/var/log/application.log")
  def record(msg: String): Unit = writer.write(s"$msg\n")
```

We can instantiate, or _construct_, a new `BasicLog` instance just by calling `BasicLog()`. For example,
```scala
lazy val log = BasicLog()
```

This lazy value, with the identifier `log`, is essentially the same as our original object, `BasicLog`. We have
made the value lazy, to mimic the instantiation lifecycle of the `BasicLog` object, but we could also eagerly
instantiate the new `BasicLog` value with:
```scala
val log = BasicLog()
```

However, as a class, it is possible to construct more than one instance of the class `BasicLog`, with the same
behavior:
```scala
val log = BasicLog()
val reportStream = BasicLog()
```

For many classes, this would be enough, but our particular example includes a `FileWriter` in the state of every
instance of the `BasicLog` class, which writes to the file `/var/log/application.log`. We would prefer to have
different `BasicLog` instances writing to different files, and we can achieve this by parameterizing the
`BasicLog` class.

```scala
class BasicLog(id: String):
  val writer: FileWriter = FileWriter(s"/var/log/$id.log")
  def record(msg: String): Unit = writer.write(s"$msg\n")
```

This is a _template_ for creating new objects

We can now construct different `BasicLog` instances which log to different files. The parameter, `id`, becomes
part of the state of each `BasicLog` instance, so it's accessible like `val`s defined within the class body, but
unlike `val`s, the parameters are not accessible from outside the class's body.

The signature of the class, `BasicLog(id: String)` in this example, looks and behaves a lot like a method, and
is called a _constructor_. Consequencly, parameters such as `id` are called _constructor parameters_.

## Templates and Types

When a class such as `BasicLog` is defined, it introduces _two_ new entities, which, in practice, are often
treated as the same thing, but it is useful to have a clear understanding of the differences. The two concepts
are,
1. a template, invoked by a constructor, defining the creation process and structure for new objects
2. a type corresponding to that template

The same name is used for both entities, which is convenient because it is not always useful to distinguish
between them. But by defining the class `BasicLog`, we introduce a constructor called `BasicLog` which
constructs objects conforming to the type called `BasicLog`. `BasicLog` is introduced as a new identifier into
both the _term_ and the _type_ namespaces.

It is also important not to confuse a class definition and an object definition: Although their bodies look
the same, only the object definition defines a new object; a class definition only defines a template or
blueprint for creating new objects. The term _template_ is not so widely used in the Scala ecosystem, perhaps
because it evokes some developers' bad memories from C++, but it's nevertheless appropriate: the definition is
a partial specification for an object, but potentially with "gaps". In the `BasicLog` example, the `id`
parameter is just such a gap, and to construct a new instance, that gap must be "filled in", that is, the `id`
parameter must be specified.

This is an important point when trying to understand the relationship between templates and types. Every
instance of a type, apart from the primitives, must have been constructed from a template, and to construct a
value, the template's parameters must have been fully specified. Looking at this from the other side, given an
instance of a type, we know that a choice of parameters must have been made in order to construct that value,
and the value's existence itself serves as evidence of this.

For example, we can reason that, if the method,
```scala
def recordInit(log: BasicLog): Unit =
  log.record("Initializing application...")
```
were called, with a `log` parameter, we would know that somewhere, that instance of `BasicLog` must have been
instantiated, and a choice of `id` parameter must have been made: after all, we expect `log` to log a message to
a file, and that file must be written with a `FileWriter`, which must have been instantiated with a filename,
and our code only ever instantiates a `FileWriter` with a location string that uses an `id` value in its
constructor parameter. But an interesting point in this example is that we cannot easily recover what that `id`
parameter was from just a `BasicLog` instance. We may access its `writer` state, but the API of `FileWriter`
does not expose any methods for accessing the file (or filename) it is writing to.

Often, this is a deliberate design choice: the object provides an abstraction over an implementation detail, and
as such, we make a choice not to expose that detail, because it _is not_, and _should not be_ important to the
users of the object.

?---?