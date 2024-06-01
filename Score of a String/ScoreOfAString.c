int scoreOfString(char *s)
{
    int sum = 0;
    int i = 1;
    while (s[i] != '\0')
    {
        sum += abs(s[i] - s[i - 1]);
        i++;
    }
    return sum;
}