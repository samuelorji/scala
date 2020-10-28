
In the programs we write, we will inevitably need to work with text, whether it's for other humans to read, or
as a carrier for computer-readable formats like JSON or XML. These sequences of characters are called _strings_,
and in Scala, they are objects with the type `String`.

There is special syntax for creating new `String` instances. The usual way to write a string in code is to place
the text between two quote characters (`"`), for example,
```scala
"The quick brown fox jumps over the lazy dog."
```

This is called a _string literal_ because we have written the text content of the string _literally_, rather
than as a reference to a string object which originates somewhere else; it's like the string is _embedded_ in
our code.

Almost any character can be included in a string literal when we write it using the style above, and we are
certainly not restricted only to the "English" alphabet, or to the widely-used ASCII character set, which
defines just 96 different characters. So this,
```scala
"სწრაფი ყავისფერი მელა ხტება ზარმაც ძაღლს."
```
is a valid Scala string literal, and so is this:
```scala
"速い茶色のキツネは怠惰な犬を飛び越えます。"
```

Strings are composed of sequences of _characters_: letters in a variety of different international alphabets,
numbers, and a huge selection of symbols and emoji characters for almost every purpose imaginable. Each
character is an atomic _glyph_, which means they can be counted, and indexed within a string, for example,
given,
```scala
val str = "Hello, World!"
```
the expression `str.length` evaluates to `13`, and `str(7)` is the character, `W`.

## Unicode

The JVM's abstraction of a string hides its internal representation from us, but it is nevertheless represented
in memory as a sequence of _Unicode codepoints_, that is, characters in the set of characters that are
representable in the _Unicode standard_.

Unicode is a set of standards which cover, primarily, a one-to-one mapping between integers and glyphs, and
secondarily, a few ways of representing sequences of those integers as binary data. The latter is known as the
_character encoding_ and will be covered in a later lesson: the JVM's representation of strings as sequences of
characters means we do not need to concern ourselves with the details of their binary representation in memory.

Scala uses the type `Char` to represents a single Unicode character. It can be readily converted to its Unicode
codepoint as an integer, and in version 13.0 of the Unicode standard (the latest version at the time of writing)
there are 143859 valid codepoints.

While every codepoint represents _something_ in the Unicode standard, not every font will provide a visible
glyph for that codepoint. String literals can still hold these values, but it may be more convenient to write
them as explicit references to Unicode codepoints. We can do this by writing the character sequence `\uxxxx` in
the string, where each `x` is a hexadecimal digit.

For example, the Greek letter, `π`, can be written inside a string literal as, `\u03c0`, because the
hexadecimal number `03c0` (which is equivalent to the decimal number `960`) corresponds to the Unicode codepoint
for `π`. We could represent the formula for the circumference of a circle as a string with either `"2πr"` or
`"2\u03c0r"`.

Note that the Unicode escape sequence always contains four hexadecimal digits, and as soon as the Scala parser
reads `\u` it knows to consume the next four characters as the Unicode codepoint.

There are a few characters which need to be treated specially to be included in a string literal, and can only
be included if they are _escaped_: written in a special way so that they can be interpreted as intended.

The quote character, `"`, if it were to appear in the middle of a string literal, would terminate the string, so
to indicate that to the Scala compiler, we need to write every `"` symbol preceded with a backslash, `\`. For
example,
```scala
"The \"quote\" character."
```


Strings in Scala are _immutable_. That means that a reference to a string will always point to the same piece