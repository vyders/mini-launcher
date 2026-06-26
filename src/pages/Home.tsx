import { FC, useState } from "react";
import { EmptyState } from "../components/EmptyState";
import { LauncherList } from "../components/LauncherList";
import { useLaunchers } from "../hooks/useLaunchers";
import { openLauncherModal } from "../utils/modal";

export const Home: FC = () => {
    const { launchers } = useLaunchers();

    const [showAddDialog, setShowAddDialog] =
        useState(false);

    if (launchers.length === 0) {
        return (
            <EmptyState
                onAdd={openLauncherModal}
            />
        );
    }

    return (
        <LauncherList
            launchers={launchers}
        />
    );
};
