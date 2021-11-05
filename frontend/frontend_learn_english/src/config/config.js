import { prodConfig } from "./prod.env";
import { devConfig } from "./dev.env";

const isProduction = true;

let config;

if (isProduction) {
  config = prodConfig;
} else {
  config = devConfig;
}

export { config };
