# ESPHome board configuration templates

Configuration templates for my ESPHome boards and devices

See also: [smkent/pcb][pcb]

## Example

To set up a board, import that board's package file in your ESPHome device
configuration.

This example creates a device using the config for my CWWW v3 board:

```yaml
packages:
  board:
    url: https://github.com/smkent/esphome-boards
    ref: main
    files:
    - boards/cwww/v3.yaml

substitutions:
  device: desk-cwww
  name: "Desk Light"
```

## Secrets

Define the following secrets in `secrets.yaml` in the same directory as your
ESPHome device YAML files:

```yaml
wifi_ssid: "Your WiFi SSID"
wifi_password: your_wifi_password
wifi_domain: .local
api_encryption_key: 32-bit_value_base64_encoded
ota_password: choose_an_ota_password_for_esphome
```


[pcb]: https://github.com/smkent/pcb
