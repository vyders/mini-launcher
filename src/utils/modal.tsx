import { createElement } from "react";
import { showModal } from "@decky/ui";

import { LauncherModal } from "../components/LauncherModal";

export function openLauncherModal() {
    console.log("Opening modal...");

    showModal(
        createElement(LauncherModal),
              undefined,
              {
                  strTitle: "Mini Launcher",
              }
    );
}
