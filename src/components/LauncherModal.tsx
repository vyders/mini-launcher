import { FC } from "react";
import {
    ModalRoot,
    DialogHeader,
    DialogBody,
    DialogButtonPrimary,
} from "@decky/ui";

interface Props {
    closeModal?: () => void;
}

export const LauncherModal: FC<Props> = ({ closeModal }) => {
    return (
        <ModalRoot closeModal={closeModal}>
            <DialogHeader>
                Add Launcher
            </DialogHeader>

            <DialogBody>
                Mini Launcher is working!
            </DialogBody>

            <DialogButtonPrimary
                onClick={() => closeModal?.()}
            >
                Close
            </DialogButtonPrimary>
        </ModalRoot>
    );
};
