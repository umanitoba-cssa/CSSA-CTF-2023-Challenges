namespace ValidatorSolution
{
    internal class Program
    {
        static void Main(string[] args)
        {
            using (var stream = new MemoryStream())
			using (var writer = new BinaryWriter(stream))
			{
				writer.Write((int) 863336819);
				writer.Write((char) 'G');
				writer.Write((byte)120);
				writer.Write((ulong) 3563299689844930872);
				writer.Write((double)9.620974397096203E+280);
				writer.Write((float)251024960);
				writer.Write((short)25973);
				writer.Write((uint)1954042440);

				stream.Position = 0;

				using (BinaryReader br = new BinaryReader(stream))
				{
					while (stream.Position < br.BaseStream.Length)
					{
						Console.Write(br.ReadChar());
					}
				}
			}
        }
    }
}