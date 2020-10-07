# Type classes

Scala provides support for _type classes_, which allow you to write and use generic code, which 
work across all data types that support a given set of capabilities.

Common examples of type classes include:

- Ordering type class. Many data types can be ordered (that is, you can say which value comes 
 before which other value).
 - Encoding & decoding type classes. Many data types can be encoded into some format like JSON or 
 XML (or decoded from such a format). 

## Definition

Type classes are _parametrically-polymorphic traits_ that describe capabilities of their type 
parameters. For example, a `trait PrettyPrint[A]` might describe the ability of some type `A` to be 
pretty-printed into a string.

Type class definitions typically include the following elements:

 - Methods that operate on values of the polymorphic types. These methods are referred to as the 
   _operations_ of the type class.
 - Constructors that build values of the polymorphic types.

In the following snippet, a type class called `PrettyPrint` is defined for a type `A`. The type 
class defines a single operation to pretty print a value of type `A`:

```
trait PrettyPrint[A]:
  def prettyPrint(value: A): String
```

## Instances

Type classes define a _contract_ that must be satisfied by data types that possess the capabilities 
described by those type classes.

To satisfy this contract for a given data type, we must define an instance of the type class for 
the type. We do this using the `given` keyword.

The `given` keyword requires that we implement the trait for a specified data type.

In the following snippet, we define an instance of `PrettyPrint` for the data type `String`:

```
given PrettyPrint[String]:
  def prettyPrint(value: String): String = value
```

Note that since type classes are traits, it is possible to create implementations of these traits
without using the `given` keyword. However, without the `given` keyword, such implementations will
not be given special treatment, and it will be necessary to manually supply these instances to 
generic code that requires them.

## Using Type Classes

Once a type class is defined, a generic method can require that some parametrically polymorphic type 
support the capabilities of the type class with a `using` parameter list, which follows all the 
value parameter lists of the method.

In this example, we define a `debug` method, which requires that the type parameter `A` support the
`PrettyPrint` type class:

```
def debug[A](a: A)(using p: PrettyPrint[A]): Unit = 
  println(s"DEGBUG: ${p.prettyPrint(a)}")
```

## Using Generic Code

Generic methods that require type classes may be invoked without manually supplying instances for 
the required type classes, assuming such instances are provided using `given`.

In the following snippet, we call `debug` on a `String`, which will succeed because we have 
previously provided an instance of the required `PrettyPrint` type class using `given`:

```
debug("Hello World!")
```

Since type classes are traits, and it is possible to create implementations of these traits without 
the `given` keyword, it is also possible to supply these values to generic code manually, with the 
`using` keyword.

In the following snippet, we construct an implementation of `PrettyPrint` for an integer, and then 
manually supply this implementation to the `debug` method so we can debug an integer literal:

```
val intPrettyPrint = 
  new PrettyPrint[Int]:
    def prettyPrint(v: Int): String = v.toString

debug(42)(using intPrettyPrint)
```

Unless absolutely necessary, it is best practice to define instances using the `given` keyword, so 
it is not necessary to manually supply trait implementations with the `using` keyword.

?---?
# Select which of the following features are provided by type classes.

- [ ] Unit tests for the operators and constructors
- [X] Operators on values of the type
- [X] Constructors for values of the type
- [ ] A family of interfaces for the type

# Choose which keyword can create a new type class:

* [ ] `class`
* [ ] `final`
* [ ] `given`
* [X] `trait`
* [ ] `using`

# Choose which keyword can create a new instance for a type class:

* [ ] `class`
* [ ] `final`
* [X] `given`
* [ ] `trait`
* [ ] `using`

# Choose which keyword can supply a manually-created implementation of a type class to a generic method:

* [ ] `class`
* [ ] `final`
* [ ] `given`
* [ ] `trait`
* [X] `using`

# Select which code snippet follows best practices:

```
// Code Snippet A
val intPrettyPrint = 
  new PrettyPrint[Int]:
    def prettyPrint(v: Int): String = v.toString 

// Code Snippet B
given PrettyPrint[Int]:
  def prettyPrint(v: Int): String = v.toString
```

 * [ ] `A`
 * [X] `B`
