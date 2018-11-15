from caffe.proto import caffe_pb2 # import the class
import caffe

#generate classified label file
def labelmap(example, result):
    labelmap = caffe_pb2.LabelMap()
    # iterate through the sample file 
    for i in range(len(example)):
        item = caffe_pb2.LabelMapItem()
        item.name = example[i]['name']
        item.label = example[i]['label']
        labelmap.item.add().MergeFrom(item)
    # writes the mapping result to the result file
    with open(result, 'w') as file:
        file.write(str(labelmap))
