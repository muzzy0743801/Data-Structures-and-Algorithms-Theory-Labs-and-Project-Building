using System;

namespace Project
{
    class Program
    {


        // A utility function to
        // print array of size n */
        public static void PrintArray(string[] array)
        {
            foreach (var item in array)
                Console.Write(item + " ");
            Console.WriteLine();
        }
        public static void PrintArray(int[] array)
        {
            foreach (var item in array)
                Console.Write(item + " ");
            Console.WriteLine();
        }

        // Driver code
        public static void Main()
        {
            string array_type = "int";
            array_type = array_type.ToLower();
            if (array_type == "string")
            {
                string[] array = new string[] { "Zaid", "Usaid", "Sumama", "Sumu", "Zaidu" };
                Console.WriteLine("Given Array");
                PrintArray(array);
                array_type = "Sorts";
                _ = new String_Class(array, array_type);
                Console.WriteLine(String_Class.Linear(array, "Sumu"));
            }
            else if (array_type == "int")
            {
                int[] array = { 12, 11, 13, 5, 6, 7 };
                Console.WriteLine("Given Array");
                PrintArray(array);
                array_type = "bucket sort";
                _ = new Int_Sorter(array_type.ToLower(), array);
                Console.WriteLine("\nSorted array");
                PrintArray(array);
            }
        }
    }
}
