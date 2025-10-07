# repo-unroll-priv
Get all non-gitignored text into context.

Simple script to get all non-gitgnored ASCII text from a repo into a single string.

It traverses each directory recurisvely and copies the relevant textual code in.

The final output looks something likes this:

```
./examples/single_string.rs:
<rust code for this example>

./examples/multiple_string.rs:
<rust code for this example.>

./src/lib.rs:
<code for the lib>

<and so on for each directory recursively>
```

Useful if for example you want to copy all of a repository and put it in chatbot.
