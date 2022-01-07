#include <stdio.h>
int main()
{
    int a, b;
    int arr1[100], arr2[100], arr3[200];
    scanf("%d %d", &a, &b);
    for (int i = 0; i < a; i++)
    {
        scanf("%d", &arr1[i]);
    }
    for (int i = 0; i < b; i++)
    {
        scanf("%d", &arr2[i]);
    }
    int m = 0; //arr1
    int n = 0; //arr2
    int k = 0; //arr3
    while (m < a && n < b)
    {
        if (arr1[m] > arr2[n])
        {
            arr3[k] = arr2[n];
            k++;
            n++;
        }
        else
        {
            arr3[k] = arr1[m];
            k++;
            m++;
        }
    }
    if (m == a)
    {
        for (int i = n - m; i < n; i++)
        {
            arr3[k++] = arr2[i];
        }
    }
    if (n == b)
    {
        for (int i = m - n; i < m; i++)
        {
            arr3[k++] = arr1[i];
        }
    }
    for (int i = 0; i < m + n; i++)
    {
        printf("%d ", arr3[i]);
    }
    return 0;
}