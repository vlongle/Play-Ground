import tensorflow as tf
import numpy as np
import time


DATA_FILE = "./birth_life.txt"


def data2Arr(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        lines = file.readlines()  # lines is a list of strings now

        # iterating over individual strings. rstrip() removes the trailing \n
        # split('\t') splits the string into individual words based on tab separation
        lines = [line.rstrip().split('\t') for line in lines]

        DATA_SIZE = len(lines)-1
        data = np.empty([2,DATA_SIZE])

        for i in range(DATA_SIZE):
            data[1][i] = lines[i+1][1] # birth rate
            data[0][i] = lines[i+1][2] # life expectancy

        return data



print("Use different loss func")

data = data2Arr(DATA_FILE)
print(len(data[0]))

# life expectancy, birth rate = X, Y
X, Y = tf.placeholder(tf.float32, name = 'X' ), tf.placeholder(tf.float32, name = 'Y' )

w, b = tf.Variable(0.0, name = 'w'), tf.Variable(0.0, name = 'b') # both scalars for simplicity

Y_predicted = tf.add(tf.multiply(X,w), b, name = "Y_predicted")

loss = tf.square(Y - Y_predicted, name='loss')

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

start = time.time()

# print(data[1])


with tf.Session() as sess:
    tf.initialize_all_variables().run()
    # tensorboard
    board = tf.summary.FileWriter('./graphs', sess.graph)


    for i in range(10):
        total_loss = 0
        for x,y in zip(data[0], data[1]):
            sess.run(loss, feed_dict={X:x, Y:y})
            total_loss += sess.run(loss, feed_dict={X:x, Y:y})

        print("total_loss:", total_loss)
        sess.run(optimizer, feed_dict={X: x, Y: y})
        print("[w,b]: ", sess.run([w, b], feed_dict={X: x, Y: y}))



    print("total_loss:", total_loss)

    # for i in range(20):
    #     for x,y in zip(data[0], data[1]):
    #         sess.run(optimizer, feed_dict={X:x, Y:y})
    #         # w,b = sess.run([w,b], feed_dict={X:x, Y:y})
    #         # training_loss = sess.run(loss, feed_dict={X:x, Y:y})
    #         # print("Optimizing", i)
    #               # "[w,b]", [w,b], "loss: ", training_loss)

    # w, b = sess.run([w,b], feed_dict={X:x, Y:y})
    board.close()

print("Final result: ", w, b)















