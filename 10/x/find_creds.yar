rule find_creds
{
    meta:
        description = "credential sweeper"
        author = "Jake Overall"
        date = "2020-11-16"
    strings:
        $username = "username" nocase
        $password = "password" nocase
        $pass = "pass" nocase
    condition:
        any of them
}