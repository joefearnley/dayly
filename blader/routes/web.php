<?php

use App\Livewire\Settings\Appearance;
use App\Livewire\Settings\Password;
use App\Livewire\Settings\Profile;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\DashboardController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\EntryController;


Route::get('/', [HomeController::class, 'index'])->name('home');

Route::middleware(['auth', 'verified'])->group(function () {
    Route::redirect('settings', 'settings/profile');

    Route::get('settings/profile', Profile::class)->name('settings.profile');
    Route::get('settings/password', Password::class)->name('settings.password');
    Route::get('settings/appearance', Appearance::class)->name('settings.appearance');

    Route::get('dashboard', [DashboardController::class, 'index'])->name('dashboard');

    Route::get('/entries', [EntryController::class, 'index'])->name('entries.index');
    Route::get('/entries/create', [EntryController::class, 'create'])->name('entries.create');
    Route::post('/entries/store', [EntryController::class, 'store'])->name('entries.store');
    Route::get('/entries/{slug}', [EntryController::class, 'show'])->name('entries.show');
    Route::get('/entries/edit/{slug}', [EntryController::class, 'edit'])->name('entries.edit');
    Route::patch('/entries/{entry}', [EntryController::class, 'update'])->name('entries.update');
    Route::delete('/entries/{entry}', [EntryController::class, 'destroy'])->name('entries.destroy');
});

require __DIR__.'/auth.php';
