---
tags:
  - js 
  - introspection 
---
# introspection

- [ ] find my you don't know js book rewrite
- [ ] a zip file and dump here

```js
console.dir(thingy)
```

## blah

JavaScript is a very loose language, but has some interesting properties. Some of them are not obvious or are quite weird.

The language uses prototype inheritance rather than the usual class inheritance from languages like Java, C++ or Python. To declare a class, you simply define a constructor function, which is really a normal function:

```js
function MyClass() {}
```

The constructor defines a new property in the global space, named MyClass. The value associated with it is a function object that does nothing in our case.

To create an instance of MyClass you simply call the constructor:

var obj = new MyClass();
The new operator will create a new JavaScriptObject and invoke the function associated with the MyClass name, passing to it as invisible argument the newly created Object instance. Inside the "constructor" function, the code can use the special this property to refer to the instance.

The following code snippet:

function MyClass() {
  this.ivar = 1;
}
creates a new property named ivar associated with the receiving Object instance.

In JavaScript all objects act as hash tables. The keys in the hash tables are the names of the "instance variables" or "properties". With the latter definition of MyClass() and the obj definition above, the following two expressions return the same object: obj.ivar and obj["ivar"].

If an instance variable is not declared and you refer to it using the this["name-of-variable"] you obtain the null value. This is nice since you can now verify if an instance variable is defined or not.

In JavaScript classes are just properties of the global scope object. The global scope is accessible through the this keyword. To obtain the MyClass object for example, you can do:

this["MyClass"]
You can also refer to the top-level obj variable with the expression:

this["obj"]
You can iterate over all the variables and classes defined in the global scope by doing:

for (i in this) print(i);
Quite nifty, huh? On the right is the JavaScript bible I use. The information above is not in it though...

Posted by ovidiu at February 26, 2004 08:24 PM |
