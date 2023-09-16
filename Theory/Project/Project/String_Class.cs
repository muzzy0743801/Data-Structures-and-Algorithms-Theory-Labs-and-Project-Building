using System;
using System.Collections.Generic;
using System.Text;


class String_Class
{
    public String_Class(string[] array, string type)
    {
        if (type == "sort")
        {
            Sort(array);
        }
        else if (type == "sorts")
        {
            Binary(array,array.Length,"Sumu");
        }
        else if (type == "linear sort")
        {
            Linear(array, "Sumu");
        }
    }
    static public string[] Sort(string[] array)
    {
        for (int i = 0; i < array.Length; i++)
        {
            for (int j = 0; j < array.Length; j++)
            {
                if (j > 0)
                {
                    if (array[j - 1].CompareTo(array[j]) > 0)
                    {
                        string temp = array[j];
                        array[j] = array[j - 1];
                        array[j - 1] = temp;
                    }
                }
            }
        }
        return array;
    }
    static public string Binary(string[] array,int value, string name)
    {
        if (value <= 1)
        {
            int l = 0;
            for (int r = array.Length - 1; l <= r;)
            {
                int m = l + (r - l) / 2;

                int checker = name.CompareTo(array[m]);

                if (checker == 0)
                    return Convert.ToString(m);

                if (checker > 0)
                    l = m + 1;

                else
                    r = m - 1;
            }
        }
        return "Not Found";
    }
    static public string Linear(string[] array, string name)
    {
        Sort(array);
        for (int i = 0; i < array.Length; i++)
        {
            if (array[i] == name)
            {
                return "Found";
            }
        }
        return "Not Found";
    }
}