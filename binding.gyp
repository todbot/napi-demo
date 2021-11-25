{
  "targets": [
    {
      "target_name": "hello",
      "sources": [ "hello.c" ],
      "conditions": [
        ["OS == 'mac'", {
          "xcode_settings": {
            # -fvisibility=hidden
            "GCC_SYMBOLS_PRIVATE_EXTERN": "YES",
            "MACOSX_DEPLOYMENT_TARGET": "10.7",
            "OTHER_CFLAGS": [
              "-arch x86_64", "-arch arm64"
            ],
            "OTHER_LDFLAGS": [
              "-arch x86_64", "-arch arm64"
            ]
          }
        }], # OS==mac
          
        ["OS == 'win'", {
        
        }], # OS==win
          
        ["OS == 'linux'", {
        
        }] # OS==linux
          
      ] # conditions
    }] # targets
}
