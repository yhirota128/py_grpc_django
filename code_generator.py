from grpc.tools import protoc

protoc.main(
    (
        '',
        '--proto_path=protos',
        '--python_out=build',
        '--grpc_python_out=build',
        # この下にビルドするprotoファイルを列挙（新規作成したら追加）
        'helloworld.proto',
    )
)
