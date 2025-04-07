<div class="p-4">
    <div class="flex justify-end">
        <flux:button wire:click="$dispatch('closeModal')" class="cursor-pointer">
            <span class="sr-only">Close</span>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-4">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
            </svg>
        </flux:button>
    </div>
    <div class="p-2">
        <p class="text-red-900 font-bold">{{ $entry->date_published  }}</p>
        <p>{{ $entry->body }}</p>
    </div>
</div>
