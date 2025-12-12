# Rust Snippets for Zed (**Ultimate Edition**)
A collection of Rust snippets to improve your development speed in the Zed IDE.

## Installation
This extension is designed to work with the Zed IDE. To install it, follow these steps:

1. Clone this repo:

```shell
git clone https://github.com/timlau/zed-rust-snippets
```

2. Go to the Extensions menu in the Zed IDE
3. Click "Install Dev Extension"
4. Select the folder you cloned

## Who to use

All snippets is prefixed `ux-` and is grouped be seached fast by typing the first letter in each group
Ex.`uaf` will select the `ux-add-fn` snippet.

![pics/uaf.png](pics/uaf.png)
![pics/ux-add-fn.png](pics/ux-add-fn.png)

## Snippets

|  Snippet                |  Description                           |
|-------------------------|----------------------------------------|
|ux-add-fn                |add function/method                     |
|ux-add-fn-async          |add async function/method               |
|ux-add-fn-pub            |add pub function/method                 |
|ux-add-fn-pub-async      |add pub async function/method           |
|ux-dbg-derive            |#[derive(<traits>)]                     |
|ux-dbg-derive-plus       |#[derive(Debug, <traits>)]              |
|ux-dbg-enum              |enum with Debug derive                  |
|ux-dbg-struct            |struct with Debug derive                |
|ux-error-dev             |define Error/Result types for early dev.|
|ux-error-rs              |custom Error boilerplate                |
|ux-fn-main-async         |async main fn returning Result          |
|ux-fn-main-result        |main fn returning Result                |
|ux-for                   |for loop                                |
|ux-hashmap-entry         |append value to vector in hashmap       |
|ux-hashmap-string-vec    |define HashMap <T, Vec<U>>              |
|ux-if-some               |if let Some pattern matching            |
|ux-impl-default          |implement default() method for struct   |
|ux-impl-from             |impl From implementation for struct     |
|ux-impl-method           |impl method for struct                  |
|ux-impl-new              |impl new method for struct              |
|ux-impl-try-from         |impl TryFrom for struct (assume Result<T> in scope)|
|ux-macro-rules           |define macro_rules!                     |
|ux-match-option          |match an option statement               |
|ux-match-result          |match a result statement                |
|ux-misc-err              |Err(err)                                |
|ux-misc-err-custom       |Err(Error::)                            |
|ux-print-dbg             |debug print a value                     |
|ux-result                |Result<T>                               |
|ux-some                  |Some(value)                             |
|ux-test-fn               |test function                           |
|ux-test-fn-async         |async test function                     |
|ux-test-module           |test module boilerplate                 |
|ux-to-string             |.to_string()                            |
|ux-use-1                 |use <module>::<imports>                 |
|ux-use-2                 |use <module>::<sub-module>::<imports>   |
|ux-vec!                  |Create a new vector with values         |
|ux-vec-mut               |Create a new mutable vector             |
