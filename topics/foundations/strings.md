
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
defines just 96 different characters.

Strings are composed of sequences of _characters_: letters in a variety of different international alphabets,
numbers, and a huge selection of symbols and emoji characters for almost every purpose imaginable. Each
character is an unseparable atomic _glyph_, and we can count them.

The JVM's abstraction of a string hides its internal representation from us, but it is represented in memory as
an array of _Unicode codepoints_, that is, characters in the set of characters that are representable in the
_Unicode standard_.

Unicode is a set of standards which cover, primarily, a one-to-one mapping between integers and glyphs, and
secondarily, a few ways of representing sequences of those integers as binary data. The latter is known as the
_character encoding_ and will be covered in a later lesson.

The JVM, and hence Scala, also offer a `Char` type, which represents a single Unicode character, and which is
readily convertible to the integer corresponding to its Unicode codepoint.

There are a few characters, however, which need special treatment to be included in a string literal. The quote
character, `"`, if it were to appear in the middle of a string literal, would be 
- `"`, the quote


Strings in Scala are _immutable_. That means that a reference to a string will always point to the same piece