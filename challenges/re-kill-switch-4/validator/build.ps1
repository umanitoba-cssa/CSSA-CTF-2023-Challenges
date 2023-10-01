javac --source 8 --target 8 Main.java
jar cmvf META-INF/MANIFEST.MF validator.jar *.class
rm *.class