interface AppContextType {
    sidebarOpen: boolean;
    userInfo: { full_name: string; profile_path: string; title: string };
    openTab: (id: string, title: string, component?: React.ReactNode) => void;
    // Diğer tipler...
}