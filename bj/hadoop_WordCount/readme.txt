----0
hadoop dfs -ls [folder_path]
hadoop dfs -ls 
hadoop dfs -ls yapeng/WC/input
hadoop dfs -mkdir yapeng/WC
hadoop dfs -copyToLocal yapeng/WC/output/* ./

[@sjs_37_33 hadoopwork]# echo "foo foo quux labs foo bar quux" | ./word_count_mapper.py | sort | ./word_count_ruducer.py 
bar	1
foo	3
labs	1
quux	2
hadoop dfs -mkdir yapeng/WC
# hadoop dfs -copyFromLocal 1.txt 2.txt yapeng/WC/input

----1Haoop֧����������������̣���Ҫ�õ���ΪStreaming��ͨ��API��Haoop֧����������������̣���Ҫ�õ���ΪStreaming��ͨ��API��
Streaming��Ҫ���ڱ�д�򵥣���С��MapReduce���򣬿���ͨ���ű����Ա�̣���������ݣ���������÷�Java�⡣
HadoopStreamingʹ��Unix�е�������򽻻�����stdin�������ݣ���stdout������ݡ�ʵ���Ͽ������κ�������Ϊmapper��reducer��������ʾ�����£�

cat [intput_file] | [mapper] | sort | [reducer] > [output_file]
----2
Hadoop Streaming����ȱ��
�ŵ�
����ʹ���Լ�ϲ������������дMapReduce���򣨻��仰˵������дJava XD��
����Ҫ��дJava��MR��������importһ��ѿ⣬�ڴ�������һ������ã��ܶණ����������stdio�ϣ���������������
��Ϊû�п�����������Է��㣬���ҿ�������Hadoop���ڱ����ùܵ�ģ�����
ȱ��
ֻ��ͨ�������в���������MapReduce��ܣ�����Java�ĳ������������ڴ�����ʹ��API���������Ƚ�������Щ�����޳�Ī��
��Ϊ�м����һ�㴦��Ч�ʻ�Ƚ���
����Hadoop Streaming�Ƚ��ʺ���һЩ�򵥵����񣬱�����pythonдֻ��һ�����еĽű��������Ŀ�Ƚϸ��ӣ�������Ҫ���бȽ�ϸ�µ��Ż���ʹ��Streaming�����׳���һЩ�������ŵĵط���
----3
��streaming������ʹ��lzoѹ��
��inputformat����ΪDeprecatedLzoTextInputFormat����Ҫ���ò��� stream.map.input.ignoreKey=true��
----4



