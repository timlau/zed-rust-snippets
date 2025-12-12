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

All snippets is prefixed `1u-` and is grouped be seached fast by typing the first letter in each group
Ex.`1fmr` will select the `1u-fn-main-result` snippet.

![Snippets](pics/snippets.gif)

## Snippets

|  Snippet                |  Description                           |
|-------------------------|----------------------------------------|
|1u-add-fn                |add function/method                     |
|1u-add-fn-async          |add async function/method               |
|1u-add-fn-pub            |add pub function/method                 |
|1u-add-fn-pub-async      |add pub async function/method           |
|1u-dbg-derive            |#[derive(\<traits\>)]                   |
|1u-dbg-derive-plus       |#[derive(Debug, \<traits\>)]            |
|1u-dbg-enum              |enum with Debug derive                  |
|1u-dbg-struct            |struct with Debug derive                |
|1u-error-dev             |define Error/Result types for early dev.|
|1u-error-rs              |custom Error boilerplate                |
|1u-fn-main-async         |async main fn returning Result          |
|1u-fn-main-result        |main fn returning Result                |
|1u-for                   |for loop                                |
|1u-hashmap-entry         |append value to vector in hashmap       |
|1u-hashmap-string-vec    |define HashMap \<T, Vec\<U\>\>          |
|1u-if-some               |if let Some pattern matching            |
|1u-impl-default          |implement default() method for struct   |
|1u-impl-from             |impl From implementation for struct     |
|1u-impl-method           |impl method for struct                  |
|1u-impl-new              |impl new method for struct              |
|1u-impl-try-from         |impl TryFrom for struct (assume Result\<T\> in scope)|
|1u-macro-rules           |define macro_rules!                     |
|1u-match-option          |match an option statement               |
|1u-match-result          |match a result statement                |
|1u-misc-err              |Err(err)                                |
|1u-misc-err-custom       |Err(Error::)                            |
|1u-print-dbg             |debug print a value                     |
|1u-result                |Result\<T\>                             |
|1u-some                  |Some(value)                             |
|1u-test-fn               |test function                           |
|1u-test-fn-async         |async test function                     |
|1u-test-module           |test module boilerplate                 |
|1u-to-string             |.to_string()                            |
|1u-use-1                 |use \<module\>::\<imports\>             |
|1u-use-2                 |use \<module\>::\<sub-module\>::\<imports\>|
|1u-vec!                  |Create a new vector with values         |
|1u-vec-mut               |Create a new mutable vector             |
