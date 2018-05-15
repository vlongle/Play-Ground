import tensorflow as tf


a = tf.constant(2, name = "a")
b = tf.constant(3, name = "b")
c = tf.add(a,b, name = "c")
d = tf.multiply(c,b, name = 'd')


with tf.Session() as sess:
    print("---------Program starts -------")
    print("------------------------------------")


    writer = tf.summary.FileWriter('./graphs',sess.graph)
    print(type(sess.run(c)))
    graphDef = sess.graph.as_graph_def()
    print(len(graphDef.node))
    # print(graphDef.node[3])
    writer.close()
