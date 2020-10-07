# Type Classes Motivation

## Context

Generic programming lets us reuse code across many data types that are all similar in some well-
defined way. 

An abstraction is a precise description of the ways in which different data types share common 
structure. Abstraction allows different data types to participate in generic programming.

Scala 3 has powerful features for _abstraction_. In order to better appreciate these features, we 
will take a look at how generic programming is achieved in object-oriente dprogramming languages 
like Java.

## Duplication

In order to sort a list of integers, we can define a recursive method as shown below:

```
def sort(list: List[Int]): List[Int] = 
  list match
    case Nil => Nil 
    case head :: tail =>
      val (lessThan, notLessThan) = tail.partition(_ < head)

      sort(lessThan) ::: head :: sort(notLessThan)
```

This method, however, is not generic: we can only use it to sort lists of integers. 

This is unfortunate, because actually, there's not much difference between sorting a list of 
integers and a list of strings. In theory, we can sort a list of _anything_, so long as we know how 
to compare two values of that type to see which value comes first.

As a first step toward making this function generic, we could introduce a type parameter:

```
def sort[A](list: List[A]): List[A] = ???
```

Unfortunately, now we cannot implement this function, because we have no way to compare two values 
of  some unknown (arbitrary) type `A`.

To solve this problem, some turn to _object-oriented abstraction_: interfaces.

## Interface Abstraction

With object-oriented abstraction, we introduce an interface called `Orderable`, which has an `Order`
method on it:

```
trait Orderable[A]:
  def comesFirst(that: A): Boolean
```

Now, if we have a data type, say `Person`, then our data type may extend this interface and provide
a suitable implementation of the `comesFirst` method:

```
final case class Person(name: String, age: Int) extends Orderable[Person]:
  def comesFirst(that: Person): Boolean = 
    this.name < that.name || this.age < that.age
```

This allows us to write a fully generic implementation of the `sort` method, so long as we 
constrain the type using a _subtype bound_:

```
def sort[A <: Orderable[A]](list: List[A]): List[A] = ???
```

Now, because we know that the type `A` will extend `Orderable[A]`, we are able to call the 
`comesFirst` method on values of type `A`, allowing us to sort the list appropriately.

## Drawbacks of OO Interfaces

While object-oriented interfaces solve this problem, they have two significant drawbacks:

1. They require us to modify the inheritance hierarchy of the data types we wish to participate in 
generic programming. This is impossible for data types that we don't control, and sometimes 
inconvenient for data types we do control. Ideally, we could use any data types with generic 
programming, so long as they possessed the required structure.
2. They require us to have an object on which we can call the method. Although for sorting, we will
always call the method `comesFirst` on some object, for other generic code, we may wish to create 
values of the object without first having a value of the same type. This is common in 
deserialization code, for example.

Type classes are a feature of functional programming languages that let us address these drawbacks
by pulling the interface out of the object, and making it stand alone.

?---?
# Select the advantages of using object-oriented interfaces for generic programming.

* [X] Reuse code across different data types
* [ ] No need to change inheritance hierarchy of data types
* [ ] No need for `this` object to call methods of interface
