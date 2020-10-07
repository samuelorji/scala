# Structural Matching 

Scala offers a variety of ways to describe patterns, and much of this topic will be spent discovering these.
In the example above, we have described the simplest of patterns like `Up` and `Down`. They are just references
to values, and the `dir` value will be compared to see if it is _equal_ to each of them: first `Up`, and if
the scrutinee is not equal to `Up`, we try `Down`, and so on.

Some values can be destructured into their component parts. Imagine, for example, an enumeration representing a
color, using an RGB or CMYK model:
```scala
enum Color:
  case Rgb(red: Float, green: Float, blue: Float)
  case Cmyk(cyan: Float, magenta: Float, yellow: Float, key: Float)
```

If our scrutinee is an `Rgb` value, we can match against a pattern which, at the same time as matching, extracts
the `red`, `green` and `blue` components from the value. Similarly, for a `Cmyk` value.

Here is a simple implementation of a method which converts a `Color` value into a monochrome (`Black` or
`White`) value:

```scala
enum Mono:
  case Black, White

def monochrome(color: Color): Mono =
  color match
    case Rgb(red, green, blue) =>
      if red + green + blue < 1.5 then Black else White
    case Cmyk(cyan, magenta, yellow, key) =>
      if key > 0.5 then Black else White
```

Our first case matches on a general `Rgb` value, which we write, not as a single value, but in the same way we
would construct a new instance of the enum value `Rgb`. But instead of putting known `red`, `green` and `blue`
parameters _into_ an `Rgb` constructor, we are going to extract them _out of_ the enum value. And those values,
called `red`, `green` and `blue` are newly available to use on the right-hand side of the case clause, set to
whichever values the `Rgb` instance was initialized with.

So while pattern matching against a single value would perform an _equality check_ between that value and the
scrutinee, a structural match will check that the scrutinee has the right structure—in this example, checking
that it is an `Rgb` instance of the `Color` type.

`case Rgb(red, green, blue)` is a simple example of a pattern _destructuring_ the scrutinee into its component
parts, `red`, `green` and `blue`. We can choose any name for the three parameters, so `case Rgb(r, g, b)` would
be an alternative way of writing the same pattern, but it would extract the color values into identifiers called
`r`, `g` and `b` instead. There is no need for the extracted components' names to match the names in the
definition of `Rgb`.

## Nested Structures

Imagine if we wanted to represent a circle, with a center, a radius and a color. In addition to our definition
of `Color`, we could define these case classes to model the data.
```scala
case class Point(x: Double, y: Double)
case class Circle(position: Point, radius: Double, color: Color)
```

Much like matching on an instance of `Rgb`, we could match on an instance of `Circle`, in a method which finds
the *x*-coordinate of the furthest left extent of the circle, which will be one _radius_ to the left of the
center of the circle.

```scala
def leftEdge(circle: Circle): Double =
  circle match
    case Circle(center, radius, color) => center.x - radius
```

This introduces, on the right-hand side of the case clause, three new identifiers called `center` (an instance
of `Point`), `radius` and `color`, an `Rgb` instance. But these can additionally be treated as nested scrutinees
against which we can pattern match by substituting nested patterns in place of their identifiers, like so:
```scala
def leftEdge(circle: Circle): Double =
  circle match
    case Circle(Point(x, y), radius, Rgb(r, g, b)) =>
      x - radius
```

In this particular expression, only the *x*-coordinate and the radius are used on the right-hand side of the
case clause, so we don't need to bind names to the parameters we do not use; there is usually no point in having
more identifiers in scope than necessary. We can use an underscore (`_`) as a placeholder for any parameters we
are not interested in, though we are still required to acknowledge their existence—every pattern must have the
correct number of parameters!

Here is the rewritten method:
```scala
def leftEdge(circle: Circle): Double =
  circle match
    case Circle(Point(x, _), r, _) => x - r
```

We took the opportunity to rename `radius` to `r`, since `r` is no longer used for the red component of the
RGB color. It would have been an error if we had attempted to bind both parameters to the same identifier, `r`.

Sometimes, in an expression like the example above, we would like to both destructure a pattern, _and_ bind it
to an identifier. Imagine that we wanted to resize all the circles whose centers lie exactly on the *x*-axis
or the *y* axis, so that their radii are `1`, and leave the others unchanged.

An implementation might look like this:
```scala
def axisCircle(circle: Circle): Circle =
  circle match
    case Circle(Point(0, y), _, c) => Circle(Point(0, y), 1, c)
    case Circle(Point(x, 0), _, c) => Circle(Point(x, 0), 1, c)
    case other                     => other
```

Note that the first two cases have the same _structure_, but the first parameter of the `Point` is explicitly
specified as the value `0`. That means that if the *x*-coordinate of the center point extracted from the
scrutinee is not equal to `0`, then the entire case will fail to match, and evaluation will continue to check
against the next case.

We match on circles whose centres have either their *x*- or *y*-coordinates equal to `0` and construct new
circles with the same color, but a new radius of `1`. But this code also constructs new instances of `Point`s
even though the `Point` instances we matched upon do not change, even though the `Color` instances (`c`) are
reused: the value we extract from the `Circle` is exactly the same object we use in the construction of the new
`Circle` on the right-hand side of the case matches.

As the `center` value for each new circle is left unchanged, we would prefer to reuse the same value, without
constructing a new `Point` instance, and thankfully, we can pattern match on a scrutinee's structure at the
same time as binding it to an identifier, using the `@` operator to attach the identifier to the pattern. Here
is the example above rewritten more concisely:
```scala
def axisCircle(circle: Circle): Circle =
  circle match
    case Circle(pt@Point(0, y), _, c) => Circle(pt, 1, c)
    case Circle(pt@Point(x, 0), _, c) => Circle(pt, 1, c)
    case other                        => other
```

Patterns may be nested within other patterns any number of times, as deeply as we like. It is no coincidence
that destructuring a value looks very similar to constructing a new value. Compare the construction and
deconstruction of the shape value here:
```scala
val shape = Circle(Point(3.2, -1.4), 2.0, red)

shape match
  case Circle(Point(x, y), 2.0, _) =>
```

The basic structure is the same. But the pattern has the flexibility to have some values precisely specified
(for example, `2.0`), and others left unspecified (but matched and bound to identifiers) while some are marked
with an underscore to indicate they are irrelevant for the purposes of the match. The constructor, on the other
hand, must have every parameter specified, though unlike a pattern, those parameters may be _expressions_ which
are evaluated to supply a value.

Scala's structural matching provides a lot of flexibility for matching against structured data, specifying the
parts we care about and ignoring those we don't. And it employs a readable syntax which closely mirrors the
construction of the values we want to match against.

?---?
# Choose the integer value which gets returned from the call to `retrieve`, below
```scala
enum Node:
  case Duo(a: Node, b: Node)
  case Value(i: Int)

import Node._

def retrieve(duo: Duo): Int = duo match
  case Duo(Duo(a1, a2), Value(3)) =>
    a1
  case Duo(Duo(a1, a2), Duo(b1, b2)) =>
    b1
  case Duo(left: Duo, right) =>
    retrieve(left)
  case node =>
    7

retrieve(Duo(Duo(3, 4), Duo(5, 6)))
```
- [ ] 3
- [ ] 4
- [X] 5
- [ ] 7

# Tick all of the statements that are true about the following code:
```scala
enum Country:
  case Fr, De, Uk, Es, It

case class Address(street: String, city: String, postalCode: String, country: Country)
case class Label(addressees: List[String], address: Address)

enum Entity:
  case Person(name: String, address: Address)
  case Company(name: String, director: Person, address: Address)

import Country._, Entity._

def envelope(entity: Entity): Label = entity match
  case Company(name, director, address@Address(street, "Paris", postcode, Fr)) =>
    Label(List(director.name, "Director", name), address)
  case Person(name, address) =>
    Label(List(name), address)
```
 * [X] we could replace `street` with an underscore without changing the behavior of `envelope`
 * [ ] if `entity` is a `Company`, the pattern will _always_ check for equality between the `country` parameter
       and the value `Fr`
 * [X] it is possible to find an entity which does not match any of the cases in the match
 * [X] one use of the identifier `director` is shadowing another identifier with the same name
 