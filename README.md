# What

This tool will generate potential passwords from a list of tokens.
Tokens in this case are words you believe to be in some location of the password.
You may tokenize the password **MyCoolPass!** into 4 separate tokens such as **My**, **Cool**, **Pass** and **!**. But you may also tokenize into only 3 tokens with **My**, **CoolPass** and **!**. It's all subjective, so please pick appropriately.

The tool does not try the passwords for you, you'll have to find another tool for that or do it manually. Because of that, for now this tool does not alter case or offer other variations of the tokens as this would create a huge list of potential passwords with no easy way to try them.


# Usage

You run the software by doing `python GeneratePasswords.py <PATH_TO_TEXT_FILE_WITH_TOKENS>`

## Simple tokens

If you believe the words **Password** **123** **!** are in your password, but not sure in which order you'd put them in a text file like this:

```
Password
123
!
```

Through permutation the software will then output this:

```
Password123!
Password!123
123Password!
123!Password
!Password123
!123Password
```

The more tokens you supply, the more potential passwords you'll get.

## Alternative tokens

You may not be sure which exact token is in the password so you can supply alternatives by writing them on the same line. Alternatives will never be tried together:

```
Password Pass
123 123 1234
! .
```

which will then give:

```
Password123!
Password123.
Password123!
Password123.
Password1234!
Password1234.
Password!123
Password!123
Password!1234
Password.123
Password.123
Password.1234
Pass123!
Pass123.
Pass123!
Pass123.
Pass1234!
Pass1234.
Pass!123
Pass!123
Pass!1234
Pass.123
Pass.123
Pass.1234
123Password!
123Password.
123Pass!
123Pass.
123!Password
123!Pass
123.Password
123.Pass
123Password!
123Password.
123Pass!
123Pass.
123!Password
123!Pass
123.Password
123.Pass
1234Password!
1234Password.
1234Pass!
1234Pass.
1234!Password
1234!Pass
1234.Password
1234.Pass
!Password123
!Password123
!Password1234
!Pass123
!Pass123
!Pass1234
!123Password
!123Pass
!123Password
!123Pass
!1234Password
!1234Pass
.Password123
.Password123
.Password1234
.Pass123
.Pass123
.Pass1234
.123Password
.123Pass
.123Password
.123Pass
.1234Password
.1234Pass
```

Similarly, the more alternatives you supply, the more potential passwords you'll get.

## Ordered tokens

You can reduce the potential passwords by forcing tokens to be only at the beginning or the end. Going back to our original example:

```
^Password ^Pass
123 123 1234
$! $.
```

would give:

```
Password123!
Password123.
Password123!
Password123.
Password1234!
Password1234.
Pass123!
Pass123.
Pass123!
Pass123.
Pass1234!
Pass1234.
```

which will be much faster to try.

Because of those 2 keywords though, if you have them in the beginning of your tokens you will need to protect those with **\**, ie:

```
^Password ^Pass
\$123 \$123 \$1234
$! $.
```

will give

```
Password$123!
Password$123.
Password$123!
Password$123.
Password$1234!
Password$1234.
Pass$123!
Pass$123.
Pass$123!
Pass$123.
Pass$1234!
Pass$1234.
```
