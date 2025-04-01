import AppLayout from '@/layouts/app-layout';
import { type BreadcrumbItem } from '@/types';
import { Head } from '@inertiajs/react';

const breadcrumbs: BreadcrumbItem[] = [
    {
        title: 'Dashboard',
        href: '/dashboard',
    },
    {
        title: 'Entries',
        href: '/entries',
    },
];

export default function EntriesIndex({ entries }: { entries: any[] }) {
    return (
        <AppLayout breadcrumbs={breadcrumbs}>
            <Head title="Entries" />
            <div className="flex h-full flex-1 flex-col gap-4 rounded-xl p-4">
                { entries && entries.map( (entry) => (
                    <div key={entry.id}>
                        <h2>{entry.date_published}</h2>
                        <p>{entry.body}</p>
                    </div>
                )) }
            </div>
        </AppLayout>
    );
}
