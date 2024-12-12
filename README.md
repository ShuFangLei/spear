README.md

# SPEAR: Distributed AI Agent Platform

SPEAR is an advanced AI Agent platform designed to support multiple runtime environments. It provides flexibility and scalability for running AI agent workloads in various configurations. SPEAR is currently in development, with ongoing features and improvements.

## Features
## Features
<table border="1" cellspacing="0" cellpadding="10" style=" width: 100%;">
  <tr>
    <td style="width: 30%; font-weight: bold;">Features</td>
    <td style="width: 35%; font-weight: bold;">Support</td>
    <td style="width: 35%; font-weight: bold;">Status</td>
  </tr>
  <tr>
    <td rowspan="4" style="font-weight: bold;">Runtime Support</td>
    <td>Process</td>
    <td>✅ Supported</td>
  </tr>
  <tr>
    <td>Docker Container</td>
    <td>✅ Supported</td>
  </tr>
  <tr>
    <td>WebAssembly</td>
    <td>❌ Not supported</td>
  </tr>
  <tr>
    <td>Kubernetes</td>
    <td>❌ Not supported</td>
  </tr>
  <tr>
    <td rowspan="2" style="font-weight: bold;">Operating Modes</td>
    <td>Local Mode</td>
    <td>✅ Supported</td>
  </tr>
  <tr>
    <td>Cluster Mode</td>
    <td>❌ Not supported</td>
  </tr>
  <tr>
    <td style="font-weight: bold;">Deployment</td>
    <td>Auto Deployment</td>
    <td>⏳ Work in Progress</td>
  </tr>
  <tr>
    <td rowspan="3" style="font-weight: bold;">Agent Service</td>
    <td>Planning</td>
    <td>❌ Not supported</td>
  </tr>
  <tr>
    <td>Memory</td>
    <td>❌ Not supported</td>
  </tr>
  <tr>
    <td>Tools</td>
    <td>⏳ Work in Progress</td>
  </tr>
</table>


- **Runtime Support**:
  - Process
  - Docker Container
  - *Future Support*: WebAssembly and Kubernetes (K8s)
  
- **Operating Modes**:
  - **Local Mode**: Run a single AI agent workload on a local machine.
  - **Cluster Mode**: Designed to support AI agent workloads across multiple clusters. *(Not yet implemented)*




## Build Instructions

To build SPEAR and its related components, run the following command:

```bash
make
```

This command will:
 - Compile all required binaries.
 - Build Docker images for the related AI Agent workloads.

## Usage

To run SPEAR in local mode, use the following command:

```bash
export OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
bin/worker exec -n pyconversation
```

This command will:
 - Start the SPEAR worker process in local mode.
 - Run the AI agent workload with an ID of 6. (pyconversation-local)

Also, you need to set the environment variable `OPENAI_API_KEY` to your OpenAI API key. In the future, we will support other LLM providers.

## Dependencies
  PortAudio is required for the audio processing component. To install PortAudio on MacOS, use the following command:
  
  ```bash
  brew install portaudio
  ```

## Development Status

 Supported Runtimes:
 - Process
 - Docker Container
 - Planned Runtimes:
 - WebAssembly
 - Kubernetes
 
 Supported Platforms:
 - Currently developed and tested only on macOS.
 - Other platforms have not yet been tested or supported.

## Future Plans

 - Implementation of cluster mode to enable distributed AI agent workloads across multiple clusters.
 - Expansion of runtime support to include WebAssembly and Kubernetes.
 - Cross-platform support for environments beyond macOS.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to discuss new features, bug fixes, or enhancements.

## License

This project is licensed under the Apache License 2.0.
