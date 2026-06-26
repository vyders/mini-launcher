import { FC } from "react";
import {
    PanelSection,
    PanelSectionRow,
    ButtonItem,
} from "@decky/ui";

interface Props {
    onAdd: () => void;
}

export const EmptyState: FC<Props> = ({ onAdd }) => {
    return (
        <PanelSection title="Mini Launcher">
            <PanelSectionRow>
                <div>No launchers found.</div>
            </PanelSectionRow>

            <PanelSectionRow>
                <div>Create your first launcher.</div>
            </PanelSectionRow>

            <PanelSectionRow>
                <ButtonItem
                    layout="below"
                    onClick={() => {
                        console.log("Add Launcher clicked");
                        onAdd();
                    }}
                >
                    Add Launcher
                </ButtonItem>
            </PanelSectionRow>
        </PanelSection>
    );
};
