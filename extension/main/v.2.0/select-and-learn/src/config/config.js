import { prodConfig } from "./prod.env";
import { devConfig } from "./dev.env";

const isProduction = false;

let config;

if (isProduction) {
  config = prodConfig;
} else {
  config = devConfig;
}

export { config };
