# BNF Colchita

```
<exp> ::= <name> | <name> (<actuals>) | turn (<exp>) | sew (<exp>,<exp>) | let <decls> in <exp> end 
<actuals> ::= <exp> | <exp> , <actuals>
<decls> ::= <decl> | <decl> <decls>
<decl> ::= fun <name> (<formals>) = <exp> | val <name> = <exp>
<formals> ::= <name> | <name> , <formals>
<name> ::= chars | chars <name>
```

> chars pasa a ser un terminal por lo que no se puede derivar

```
<chars> ::= a ... Z
```