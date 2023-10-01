namespace Validator
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                string key = args[0];

                using (var stream = new MemoryStream())
                {
                    var writer = new StreamWriter(stream);
                    writer.Write(key);
                    writer.Flush();
                    stream.Position = 0;

                    using (BinaryReader br = new BinaryReader(stream))
                    {
                        Assert(br.ReadInt32() == 863336819);
                        Assert(br.ReadChar() == 'G');
                        Assert(br.ReadByte() == 120);
                        Assert(br.ReadUInt64() == 3563299689844930872);
                        Assert(br.ReadDouble() == 9.620974397096203E+280);
                        Assert(br.ReadSingle() == 251024960);
                        Assert(br.ReadInt16() == 25973);
                        Assert(br.ReadUInt32() == 1954042440);

                        Console.WriteLine("true");
                    }
                }
            } catch (Exception)
            {
                Console.WriteLine("false");
            }
        }

        static void Assert(bool condition)
        {
            if (!condition) throw new Exception();
        }
    }
}