# 121COMWeek3ExTask
121COM Week 3 Extended Task - Quandl

The main function defined is "getFromQuandl".  This has two mandatory arguments:
  dCode (string) -- A Quandl database code
  tCode (string) -- A Quandl table code
and the following Keyword (optional) arguments:
    out (string) --- Default is "data".  Can also use "dict" if the full dictionary of information is desired.
    printInfo (boolean) --- whether to print some basic information
    printData (boolean) --- whether to print full data set.
    authCode (string) --- a Quandl authorisation code.

Read comments in the script for more details.  Play around until you understand what the different inputs do.

When you write your own script you should extend this ReadMe as appropriate.

Note: Quandl usually allows 50 requests a day for unregistered users.  However, if you find your requests are restricted you can register for free and then make 2000 requests a minute.  You can register at: 
https://www.quandl.com/users/sign_up
and then use the authentication key they email you as an optional argument to "getFromQuandl"  .
