#!/usr/bin/env bash

# by winDy
# grpc 를 위한 python 코드를 자동으로 생성한다.

echo "Generating python grpc code from proto...."
echo "into > " $PWD
python3 -m grpc.tools.protoc -I'./protos' --python_out='.' --grpc_python_out='.' './protos/train02.proto'
echo ""
