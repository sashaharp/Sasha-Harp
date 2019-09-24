#### Method 1: with prototype
 
use Win32::API;
$function = Win32::API::More->new(
    'mydll', 'int sum_integers(int a, int b)'
);
#### $^E is non-Cygwin only
die "Error: $^E" if ! $function;
#### or on Cygwin and non-Cygwin
die "Error: ".(Win32::FormatMessage(Win32::GetLastError())) if ! $function;
####
$return = $function->Call(3, 2);
 
#### Method 2: with prototype and your function pointer
 
use Win32::API;
$function = Win32::API::More->new(
    undef, 38123456, 'int name_ignored(int a, int b)'
);
die "Error: $^E" if ! $function; #$^E is non-Cygwin only
$return = $function->Call(3, 2);
 
#### Method 3: with parameter list 
 
use Win32::API;
$function = Win32::API::More->new(
    'mydll', 'sum_integers', 'II', 'I'
);
die "Error: $^E" if ! $function; #$^E is non-Cygwin only
$return = $function->Call(3, 2);
    
#### Method 4: with parameter list and your function pointer
 
use Win32::API;
$function = Win32::API::More->new(
    undef, 38123456, 'name_ignored', 'II', 'I'
);
die "Error: $^E" if ! $function; #$^E is non-Cygwin only
$return = $function->Call(3, 2);
 
#### Method 5: with Import (slightly faster than ->Call)
 
use Win32::API;
$function = Win32::API::More->Import(
    'mydll', 'int sum_integers(int a, int b)'
);
die "Error: $^E" if ! $function; #$^E is non-Cygwin only
$return = sum_integers(3, 2);